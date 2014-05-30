# btcd packaging


## binaries
[https://bitcoin-gateway.com/downloads/](https://bitcoin-gateway.com/downloads/)

## apt repository
* Add repo:
    sudo apt-add-repository 'deb http://bitcoin-gateway.com/ubuntu saucy main'
* Add key to verify:
    wget -O- http://bitcoin-gateway.com/downloads/signing-key.asc | sudo apt-key add -
* Update packages
    sudo apt-get update

## signing key
[https://bitcoin-gateway.com/downloads/signing-key.asc/](https://bitcoin-gateway.com/downloads/signing-key.asc)
