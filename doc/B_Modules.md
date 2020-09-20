# General Modules
pashmak has some general libraries to use. that modules are helpful for you.

## how to import module
you can import modules with `include` operation.

look at this example:

```bash
mem '@hash'; include ^;
mem '@time'; include ^;
mem '@module_name'; include ^;
# ...
```

you have to give name of module with a `@` before that to the include operation.

### hash module
with hash module, you can calculate hash sum of values:

```bash
mem '@hash'; include ^;

mem 'hello'; call hash.sha256; # also you can use hash.md5 and...
out ^; # output: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

###### how it works?
first, you have to put the value into the mem. next, call `hash.sha256` alias to calculate sha256 hash. then, this alias calculates hash sum and puts that into the mem. now you can access sum of that from mem.

also you can use `hash.md5` aliases and...

### time module
with this module, you can work with time.

###### time.time
this alias gives you current UNIX time:

```bash
mem '@time'; include ^;

time.time; # this is shorter of `call time.time`
out ^; # output is some thing like this: `1600416438.687201`
```

when you call this alias, this alias puts the current unix time into mem and you can access and use that from mem.

###### time.sleep
this alias sleeps for secounds:

```bash
mem '@time'; include ^;

mem 2; time.sleep; # sleepss for 2 secounds
# mem 2.4; time.sleep; # sleepss for 2.4 secounds
```

when you run this script, program waits for 2 secounds and then will finished

with this alias, you can wait for secounds.

you have to put a int or float into mem and next call `time.sleep` alias, then program will sleep for value of `mem` as secounds

### more modules comming soon...