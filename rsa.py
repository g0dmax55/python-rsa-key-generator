#!/bin/python3

#coded by g0dmax55

from Crypto.PublicKey import RSA


key = RSA.generate(2048)


def privkey():
	private_key = key.export_key()
	file_out = open("private-key.pem", "wb")
	file_out.write(private_key)
	file_out.close()

def pubkey():
	public_key = key.publickey().export_key()
	file_out = open("public-key.pem", "wb")
	file_out.write(public_key)
	file_out.close()

privkey()
pubkey()
