from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from sage.all import GCD, Integers

def RSA_encrypt():
    # Public exponent
    e = 0x10001

    # Primes
    p = getPrime(2048)
    q = getPrime(2048)
    phi = (p-1)*(q-1)

    # Ensure phi and e are coprime
    while GCD(phi, e) != 1:
        p = getPrime(2048)
        q = getPrime(2048)
        phi = (p-1)*(q-1)
    
    # Public Modulus
    N = p*q

    # Sage Integer Rings
    R_N = Integers(N)
    R_phi = Integers(phi)

    # Private Key
    d = 1/R_phi(e)

    # Get message to encrypt
    print('\nWelcome to the RSA encryptor')
    m_str = input('What message would you like to encrypt? ')
    m_long = bytes_to_long(m_str.encode())

    # Calculate ciphertext
    ct = R_N(m_long)**e

    print(f'\nEncrypted message:\n\tct = {ct}')
    print('\nPrivate information:')
    print(f'\td = {d}')
    print('\nPublic information:')
    print(f'\te = {e}')
    print(f'\tN = {N}')

    print('Would you like to save this output to a file? [y/n]')
    op = input('> ')
    while op != 'y' and op != 'n':
        print('Invalid input!')
        op = int(input(' > '))
    
    if op == 'y':
        file_name = input('What would you like to name the file? ')
        lines = [f'd={d}', f'e={e}', f'N={N}', f'ct={ct}']
        with open(f'./{file_name}.txt', 'w') as f:
            f.write('\n'.join(lines))



def RSA_decrypt():
    print('What is the public exponent value (e)? [Decimal only]')
    e = int(input('> '))
    
    N = print('What is the public modulus value (N)? [Decimal only] ')
    N = int(input('> '))

    print('What is the private key (d)? [Decimal only]')
    d = int(input('> '))

    RN = Integers(N)
    e_r = RN(e)
    m_long = e_r**d
    m_str = long_to_bytes(int(m_long)).decode('utf-8')
    print(f'Decrypted Message:\n\t{m_str}')

if __name__ == "__main__":
    print('What would you like to do?\n[0] : Encrypt\n[1] : Decrypt')
    op = int(input('> '))
    while op != 0 and op != 1:
        print('Invalid input!')
        op = int(input(' > '))
    
    if op == 1:
        print('Starting RSA decryptor...')
        RSA_decrypt()
    else:
        print('Starting RSA encryptor...')
        RSA_encrypt()