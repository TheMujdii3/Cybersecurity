The web ide runs the Rugina fork of the rust at first glance (well yeah i already had fun with this in my free time)
In reality is it just a list full of macros in romanian of the Rust language and i explained that to chatgpt and i got one genius
idea: to compile-time features to leak flag via errors using the following script: 

`
principal() { } //without a main code it will throw a compilation error                  
compile_error!(include_str!("/flag.txt"));
`



