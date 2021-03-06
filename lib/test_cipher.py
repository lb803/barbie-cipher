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

from cipher import Cipher, CIPHERS
import pytest


def test_cipher_default():
    cipher = Cipher()
    assert cipher.cipher == CIPHERS.get("cipher1")


def test_cipher_selection():
    cipher = Cipher("cipher1")
    assert cipher.cipher == CIPHERS.get("cipher1")

    cipher2 = Cipher("cipher2")
    assert cipher2.cipher == CIPHERS.get("cipher2")

    cipher3 = Cipher("cipher3")
    assert cipher3.cipher == CIPHERS.get("cipher3")

    cipher4 = Cipher("cipher4")
    assert cipher4.cipher == CIPHERS.get("cipher4")


def test_cipher_bad_selection():
    cipher = Cipher("foobar")
    assert cipher.cipher is None


def test_letter_sub():
    letter1 = Cipher.letter_sub(Cipher, "W", CIPHERS.get("plain"),
                                CIPHERS.get("cipher1"))
    assert letter1 == "."

    letter2 = Cipher.letter_sub(Cipher, "W", CIPHERS.get("plain"),
                                CIPHERS.get("cipher2"))
    assert letter2 == "M"

    letter3 = Cipher.letter_sub(Cipher, "W", CIPHERS.get("plain"),
                                CIPHERS.get("cipher3"))
    assert letter3 == "Z"

    letter4 = Cipher.letter_sub(Cipher, "W", CIPHERS.get("plain"),
                                CIPHERS.get("cipher4"))
    assert letter4 == "B"


def test_letter_fallback_sub():
    # the symbol ?? is not in the cipher
    letter = Cipher.letter_sub(Cipher, "??", CIPHERS.get("plain"),
                               CIPHERS.get("cipher1"))
    assert letter == "??"


def test_code_msg():
    cipher = Cipher()
    assert cipher.code("Fig rolls") == "Ctx nrbbf"


def test_code_empty_msg():
    cipher = Cipher()
    assert cipher.code("") == ""


def test_code_msg_typeerror():
    with pytest.raises(TypeError):
        cipher = Cipher()
        coded_msg = cipher.code(None)


def test_decode_msg():
    cipher = Cipher()
    assert cipher.decode("Ctx nrbbf") == "Fig rolls"


def test_decode_empty_msg():
    cipher = Cipher()
    assert cipher.decode("") == ""


def test_decode_msg_typeerror():
    with pytest.raises(TypeError):
        cipher = Cipher()
        decoded_msg = cipher.decode(None)
