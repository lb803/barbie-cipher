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

        if self.cipher is None:
            raise ValueError(f"The requested cipher '{cipher} does not exist")

        self.code_table = self.make_table(CIPHERS.get("plain"), self.cipher)
        self.decode_table = self.make_table(self.cipher, CIPHERS.get("plain"))

    def make_table(self, source: dict, destination: dict) -> dict:
        """Create a translation table from source to destination"""
        return str.maketrans(source, destination)

    def letter_sub(self, letter: str, table: dict) -> str:
        """Perform letter substitution using the given translation table"""
        return letter.translate(table)

    def code(self, msg: str) -> str:
        """Code message with one of the ciphers"""
        return "".join(self.letter_sub(x, self.code_table) for x in msg)

    def decode(self, msg: str) -> str:
        """Decode message with one of the ciphers"""
        return "".join(self.letter_sub(x, self.decode_table) for x in msg)
