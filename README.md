# Premium Loafers, Built Cheap


## TODO
- [ ] Ensure names are unique in project
- [ ] Disallow 'global' as a tag since it's implied
- [ ] Disallow 'global' as artifact name since it's tag
- [ ] Allow grouping artifacts to share object files
- [ ] Allow specifying custom build steps other than compile / link / run
- [x] Allow custom compile calls? (cc & ld)
- [x] Allow LDFLAGS and CFLAGS?
- [ ] Document config schema
- [x] Proper command line args (verbose, which steps to run)
- [ ] If a script requires something, it will only be built with the stage set
      by command line flags. Need a `<requires stage="compile">artifact_name</requires>`