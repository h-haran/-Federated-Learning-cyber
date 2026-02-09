import os

# Generate a random salt (16 bytes is typical)
salt = os.urandom(16)

# Save it to a file
with open("salt.bin", "wb") as f:
    f.write(salt)

print("Salt file created and saved as salt.bin")