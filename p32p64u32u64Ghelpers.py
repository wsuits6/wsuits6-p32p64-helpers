# pwntools provides these 
# built-in. Implementing manually
# builds understanding.

# Struct Library
import struct


def p32(val, sign=False): return struct.pack("<i" if sign else "<I", val)
def p64(val, sign=False): return struct.pack("<q" if sign else "<Q", val)
def u32(data, sign=False): return struct.unpack("<i" if sign else "<I", data[:4])[0]
def u64(data, sign=False): return struct.unpack("<q" if sign else "<Q", data[:8])[0]

print(p32(0xdeadbeef).hex())
 # efbeadde
print(p64(0xdeadbeef).hex())
 # efbeadde00000000
print(hex(u32(b"\xef\xbe\xad\xde")))
 # 0xdeadbeef
print(hex(u64(b"\xef\xbe\xad\xde\x00\x00\x00\x00"))) # 0xdeadbeef