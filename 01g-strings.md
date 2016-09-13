
## String processing in Tor ##

Since you're reading about a C program, you probably expected this
section: it's full of functions for manipulating the (notoriously
dubious) C string abstraction.

### Comparing strings and memory chunks ###

We provide strcmpstart() and strcmpend() to perform a strcmp with the start
or end of a string.

	tor_assert(!strcmpstart("Hello world","Hello"));
	tor_assert(!strcmpend("Hello world","world"));

	tor_assert(!strcasecmpstart("HELLO WORLD","Hello"));
	tor_assert(!strcasecmpend("HELLO WORLD","world"));

To compare two string pointers, either of which might be NULL, use
strcmp_opt().

To search for a string or a chunk of memory within a non-null
terminated memory block, use tor_memstr or tor_memmem respectively.

We avoid using memcmp() directly, since it tends to be used in cases
when having a constant-time operation would be better.  Instead, we
recommend tor_memeq() and tor_memneq() for when you need a
constant-time operation.  In cases when you need a fast comparison,
and timing leaks are not a danger, you can use fast_memeq() and
fast_memneq().

