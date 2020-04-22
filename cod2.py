import binascii
import hashlib
import struct
import random



def get_block_header(version, prev_block, mrkl_root, timestamp, bits, nonce):
    header = (struct.pack("<L", version) +
            binascii.unhexlify(prev_block)[::-1] +
            binascii.unhexlify(mrkl_root)[::-1] +
            struct.pack("<LLL", timestamp, bits, nonce)
    )
    return header
version =  0x20400000
prev_block = "00000000000000000006a4a234288a44e715275f1775b77b2fddb6c02eb6b72f"
mrkl_root = "2dc60c563da5368e0668b81bc4d8dd369639a1134f68e425a9a74e428801e5b8"
timestamp = 0x5DB8AB5E
bits = 0x17148EDF
exp = bits >> 24
mant = bits & 0xffffff
target_hexstr = '%064x' % (mant * (1 << (8 * (exp - 3))))
target_str = binascii.unhexlify(target_hexstr)


nonce = 3000000000

while nonce < 3100000000:
    header_block = get_block_header(version, prev_block, mrkl_root, timestamp, bits, nonce)
    hash1 = hashlib.sha256(hashlib.sha256(header_block).digest()).digest()
    hash = hash1[::-1]

    print("nonnce = "+str(nonce)+ "  hash:"+ str(binascii.hexlify(hash)))
    if hash < target_str:
        #logging.getLogger().info('Block hash found with succes!')
        print('succes')
        break
    nonce += 1