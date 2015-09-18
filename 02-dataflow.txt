
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
BSD mbufs, or Linux skbufs, or XXXX

A connection can be enabled or disabled for a wide variety of reasons.
