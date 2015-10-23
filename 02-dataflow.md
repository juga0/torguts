
== Data flow in the Tor process

We read bytes from the network, we write bytes to the network.  For the
most part, the bytes we write correspond roughly to bytes we have read,
with bits of cryptography added in.

The rest is a matter of details.

=== Connections and buffers: reading, writing, and interpreting.

At a low level, Tor's networking code is based on "connections".  Each
connection represents an object that can send or receive network-like
events.  For the most part, each connection has a single underlying TCP
stream (I'll discuss counterexamples below).

A connection that behaves like a TCP stream has an input buffer and an
output buffer.  Incoming data is
written into the input buffer ("inbuf"); data to be written to the
network is queued on an output buffer ("outbuf").

Buffers are implemented in buffers.c.  Each of these buffers is
implemented as a linked queue of memory extents, in the style of classic
BSD mbufs, or Linux skbufs.

A connection's reading and writing can be enabled or disabled.  Under
the hood, this fuctionality is implemented using libevent events: one
for reading, one for writing.  These events are turned on/off in
main.c, in the functions connection_{start,stop}_{reading,writing}.

When a read or write event is turned on, the main libevent loop polls
the kernel, asking which sockets are ready to read or write.  (This
polling happens in thxe event_base_loop() call in run_main_loop_once()
in main.c.)  When libevent finds a socket that's ready to read or write,
it invokes conn_{read,write}_callback(), also in main.c

These callback functions delegate to connection_handle_read() and
connection_handle_write() in connection.c, which read or write on the
network as appropriate, possibly delegating to openssl.

After data is read or written, or other event occurs, these
connection_handle_read_write() functions call logic functions whose job is
to respond to the information.  Some examples included:

   * connection_flushed_some() -- called after a connection writes any
     amount of data from its outbuf.
   * connection_finished_flushing() -- called when a connection has
     emptied its outbuf.
   * connection_finished_connecting() -- called when an in-process connection
     finishes making a remote connection.
   * connection_reached_eof() -- called after receiving a FIN from the
     remote server.
   * connection_process_inbuf() -- called when more data arrives on
     the inbuf.

These functions then call into specific implementations depending on
the type of the connection.  For example, if the connection is an
edge_connection_t, connection_reached_eof() will call
connection_edge_reached_eof().

   * NOTE: "Also there are bufferevents!"  We have a vestigial
     implementation for an alternative low-level networking
     implementation, based on Libevent's evbuffer and bufferevent
     code.  These two object types take on (most of) the roles of
     buffers and connections respectively. It isn't working in today's
     Tor, due to code rot and possible lingering libevent bugs.  More
     work is needed; it would be good to get this working efficiently
     again, to have IOCP support on Windows.


==== Controlling connections

A connection can have reading or writing enabled or disabled for a
wide variety of reasons, including:
   * Writing is disabled when there is no more data to write

   * For some connection types, reading is disabled when the inbuf is
     too full.

   * Reading/writing is temporarily disabled on connections that have
     recently read/written enough data up to their bandwidth limits.

   * Reading is disabled on connections when the circuit that their
     data would be sent to is XXXX.

