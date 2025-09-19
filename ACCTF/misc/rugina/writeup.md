# _rugina_

Category | Value
-- | --
Misc | 100

***

```rust
principal() { } compile_error!(include_str!("/flag.txt"));
```

* `principal()` is the new `main()`.
* `include_str!("/flag.txt")` reads the file **at compile time** (note the leading `/`: it’s an absolute path on the build machine).
* `compile_error!(...)` unconditionally **aborts compilation** and prints its argument as the error message.

## Proof-of-flag
```
ctf{73523e676b04e1c2db176d8035648893648b969f5ddf5ac40f8fc5b6c15d8692}
```