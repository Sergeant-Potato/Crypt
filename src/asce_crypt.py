import argparse
from cryptography.hazmat.primitives import hashes

def __hasher(passwd: str, algo: str = "SHA256", rot: int=1):

    '''
        This script generates a 256 - Bit hash of a given text. It contains three (3) parameters:
            -   password [password]: This is the 'given text'; in the context of the function, it should be a readable plain - text 
                password, such as: Test123, Test#123 or MondaytoFriday.
            -   algorithm [-ha]: This is the hashing algorithm that is to be executed by this function. Only four (4) hashing functions are accepted:
                a.  SHA256: It is default value; as well, the current golden standard due to the security it provides and the speed in which
                    it hashes a text.
                b.  SHA512-256: It is an alternative to the SHA256 golden standard; however, it takes a little more time to generate results. 
                    In this case, it produces a 256 bits digest.
                c.  SHA3-256: One the hash functions found in the SHA3 NIST Family of Standards. The SHA3 hashing algorithms is better than those
                    found in the SHA2 NIST Family of Standards; however, it is significantly slower. This is the reason why SHA256 was chosen as the
                    default value for this program. It produces a 256 - Bit digest.
                d.  SM3: This is a function standarized by the Chinese National Cryptography Administration. It produces a 256 - Bit digest. It is not
                    recomended to use this hashing algorithm.
            -   rotations [-r]: This is the number of rotations that the function will undertake on the password (initially plain - text and then hashed), to generate
                a final hashed text. It's default value is 1.
    '''
    algorithm = None
    if algo == "SHA256":
        algorithm = hashes.SHA256()
    elif algo == "SHA512-256":
        algorithm = hashes.SHA512_256()
    elif algo == "SHA3-256":
        algorithm = hashes.SHA3_256()
    elif algo == "SM3":
        algorithm = hashes.SM3()
    else:
        raise Exception("The given algorithm name is not in the list of available 256 - bit hashing algorithms.")
    
    if rot < 1 or rot > 10:
        raise Exception("The given value for the number of rotations is out of range.")
    
    for i in range(rot):
        digest = hashes.Hash(algorithm)
        digest.update(bytes(passwd, "utf-8"))
        passwd = digest.finalize().hex()
    return passwd
    
if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, 
                                     description='''
                 .88888888:.
                88888888.88888.
              .8888888888888888.
              888888888888888888
              88' _`88'_  `88888
              88 88 88 88  88888
              88_88_::_88_:88888
              88:::,::,:::::8888
              88`:::::::::'`8888
             .88  `::::'    8:88.
            8888            `8:888.
          .8888'             `888888.
         .8888:..  .::.  ...:'8888888:.
        .8888.'     :'     `'::`88:88888
       .8888        '         `.888:8888.
      888:8         .           888:88888
    .888:88        .:           888:88888:
    8888888.       ::           88:888888
    `.::.888.      ::          .88888888
   .::::::.888.    ::         :::`8888'.:.
  ::::::::::.888   '         .::::::::::::
  ::::::::::::.8    '      .:8::::::::::::.
 .::::::::::::::.        .:888:::::::::::::
 :::::::::::::::88:.__..:88888:::::::::::'
  `'.:::::::::::88888888888.88:::::::::'
        `':::_:' -- '' -'-' `':_::::'`

--------------------------------------------
-                  CRYPT.PY                -
--------------------------------------------
This script takes a given password and generates a hashed 256 - Bit version of itself. An example of the functionality is:

Plain - Text Password: 123      ==>      Hashed - Text Password: a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3.

The generated Hashed - Text version of the password is outputed on the terminal for further use.

''')
        parser.add_argument("-ha", "--hash-algorithm", default="SHA256", help='''This optional parameter denotes the type of hashing algorithm that this program will use to hash (encrypt) the password.
        The possible values that this parameter accepts are: SHA256 (Already set as default value), SHA512-256, SHA3-256, and SM3.''')
        parser.add_argument("-r", "--rotations",default=1,help='''This optional parameter sets the number of rotations; that is, the times that the password will be hashed. By default, this value is set to 1.''')
        parser.add_argument("password", help='''This required paramenter is for the password that it is wanted to be hashed (encrypted).''')
        args = vars(parser.parse_args())

        passwd = args["password"]
        algo = args["hash_algorithm"]
        rot = int(args["rotations"])

        print(__hasher(passwd=passwd,algo=algo,rot=rot))
    except Exception as e:
        print(e)
