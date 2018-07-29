# bookworm

Implementation of [Shakespeare: a sample service](https://landing.google.com/sre/book/chapters/production-environment.html#xref_production-environment_shakespeare)


we want to offer a service that lets you determine where a given word is used throughout all of Shakespeare’s works

We can divide this system into two parts:

A batch component that reads all of Shakespeare’s texts, creates an index, and writes the index into a Bigtable. This job need only run once, or perhaps very infrequently (as you never know if a new text might be discovered!).
An application frontend that handles end-user requests. This job is always up, as users in all time zones will want to search in Shakespeare’s books.
