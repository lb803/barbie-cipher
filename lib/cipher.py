#!/usr/bin/env python3
'''
Barbie Cipher - A python implementation of the Barbie Typewriter E-118
cryptographic capabilities. Copyright (C) 2022 Luca Baffa
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

CIPHERS = {"plain":    "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                       "0123456789- ' ! \" # % & ( ) * , . ¨ / : ; ? @ ^ _ + "
                       "< = > ¢ £ § €",
           "cipher1":  "icolapxstvybjeruknfhqg;dzw >FAUTCYOLVJDZINQKSEHG<.1PB"
                       "523406789-¨ _ & m @ : \" * ( # W M § ^ , ¢ / ? ! ) % "
                       "X ' R + € £ =",
           "cipher2":  "torbiudfhgzcvanqyepskx¢1w; RC>GHAPND<VUBLIKJETOYXM2QF"
                       "63405789-¨§ ) \" j ? , m # * @ . Z £ ! W + ^ / & ( : "
                       "1 _ S % = € '",
           "cipher3":  "hrnctqlpsxwogiekzaufyd+b;¢ SARYO>QIUX<GFDLJVTHNP1Z3KC"
                       "7405689-¨§£ ( m v / W j @ # ? M B € & . % ! ^ \" * , "
                       "2 ) E : ' = _",
           "cipher4":  "sneohkbufd;rxtaywiqpzl%c¢+ E>SPNRKLG1XYCUDV<HOIQ2B4JA"
                       "805679-¨§£€ * j g ^ . v ? @ / Z F = \" N : & ! m # W "
                       "3 ( T , _ ' )"
           }


class Cipher():
    def __init__(self, cipher: str = "cipher1"):
        """Define which cipher to use for message coding/decoding"""
        self.cipher = CIPHERS.get(cipher)

    def letter_sub(self, letter: str, source: str, destination: str) -> str:
        """Perform letter substitution from source to destination table"""
        table = str.maketrans(source, destination)
        return letter.translate(table)

    def code(self, msg: str) -> str:
        """Code message with one of the ciphers"""
        source = CIPHERS.get("plain")
        coded_msg = "".join(self.letter_sub(x, source, self.cipher)
                            for x in msg)
        return coded_msg

    def decode(self, msg: str) -> str:
        """Decode message with one of the ciphers"""
        destination = CIPHERS.get("plain")
        decoded_msg = "".join(self.letter_sub(x, self.cipher, destination)
                              for x in msg)
        return decoded_msg
