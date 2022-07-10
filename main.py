#!/usr/bin/env python3
'''
Barbie Cipher - A python implementation of the Barbie typewriter encryption
tables. Copyright (C) 2022 Luca Baffa
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

from lib.cipher import Cipher


def main():
    cipher = Cipher()
    plain_msg = "We run out of Jammie Dodgers."
    coded_msg = cipher.code(plain_msg)
    print(f"'{plain_msg}' codes to '{coded_msg}'")

    print(f"'{coded_msg}' decodes to '{cipher.decode(coded_msg)}'")


if __name__ == "__main__":
    main()
