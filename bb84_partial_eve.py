import random
import time

N = 50000
attack_probability = 0.1

alice_bits = [random.randint(0, 1) for _ in range(N)]
alice_bases = [random.choice(["+", "x"]) for _ in range(N)]

eve_bases = [random.choice(["+", "x"]) for _ in range(N)]
eve_bits = []

for i in range(N):
    if random.random() < attack_probability:
        if alice_bases[i] == eve_bases[i]:
            eve_bits.append(alice_bits[i])
        else:
            eve_bits.append(random.randint(0, 1))
    else:
        eve_bits.append(alice_bits[i])

bob_bases = [random.choice(["+", "x"]) for _ in range(N)]

start_time = time.time()

bob_bits = []
for i in range(N):
    if random.random() < attack_probability:
        if eve_bases[i] == bob_bases[i]:
            bob_bits.append(eve_bits[i])
        else:
            bob_bits.append(random.randint(0, 1))
    else:
        if alice_bases[i] == bob_bases[i]:
            bob_bits.append(alice_bits[i])
        else:
            bob_bits.append(random.randint(0, 1))


end_time = time.time()

alice_key = []
bob_key = []

for i in range(N):
    if alice_bases[i] == bob_bases[i]:
        alice_key.append(alice_bits[i])
        bob_key.append(bob_bits[i])

errors = sum(1 for i in range(len(alice_key)) if alice_key[i] != bob_key[i])
error_rate = errors / len(alice_key)

print("Probabilitate atac:", attack_probability)
print("QBER:", error_rate)
print("Timp executie:", end_time - start_time)
