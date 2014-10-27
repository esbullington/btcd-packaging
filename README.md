# btcd packaging
Signed btcd apt repository and signed tarballs.

----
There doesn't seem to be much interest in a signed btcd repo for apt.  However, if anyone is using this and would be interested in me updating it to the latest version of btcd and perhaps even automating the process so I could build and sign btcd nightlies, please let me know if this repo's issues.

----

### signed binary tarballs

* downloads: [https://bitcoin-gateway.com/downloads/](https://bitcoin-gateway.com/downloads/)
* signing key: [https://bitcoin-gateway.com/downloads/signing-key.asc/](https://bitcoin-gateway.com/downloads/signing-key.asc)

### apt repository
* Add repo:
    
        sudo apt-add-repository 'deb http://bitcoin-gateway.com/ubuntu saucy main'
* Download this project's signing key over https and check the full fingerprint carefully.  It should match `F3FD 461E CD16 761C 32C4  886B 1257 C84C FC93 6D9D` (Optionally, for the extra secure, you can lookup this key on any PGP keyserver and see that it's been signed by the key hosted here, which is bound to my identity: https://keybase.io/esbullington):

        wget https://bitcoin-gateway.com/downloads/signing-key.asc
        gpg --dry-run --with-fingerprint signing-key.asc
* If you're satisfied the key is a match, add it to your keychain:

        sudo apt-key add signing-key.asc
* Update packages:

        sudo apt-get update
* Install

        sudo apt-get install golang-btcd-dev
