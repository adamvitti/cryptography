#!/usr/bin/python3
# coding: latin-1
blob = """
                ���"��~�q��$|�H��~�.��!B�*.������j헋(�[�_�Y�9ЧvQ,��x^ Z��ڄ!��$Xv������4�U��/z�t;�KO���,ܰ��r?Y�k�	#d!�w���/U2�qZ��q�
"""
from hashlib import sha256 
if(sha256(blob.encode("latin-1")).hexdigest() == "a786ef51fb0c2a9d1b9068c98d3df918a43a55bcc01b087e8db6f1448681acfa"):
    print("Use SHA-256 instead!")
elif (sha256(blob.encode("latin-1")).hexdigest() == "5239bb0837859ffd3d900f7e00dc1de49262f33ce2b6404577f27b95b4c15e1a"):
    print("MD5 is perfectly secure!")
