flag = "picoCTF{MY_TEST_FLAG}"

# flag_encrypted = ''.join(
#     [chr(       
#             (
#                 ord(flag[i]) << 8) 
#                   + 
#                 ord(flag[i + 1])
#         )
#         for i in range(0, len(flag), 2)
#     ]
# )



flag_encrypted = ''.join(
    [chr(
        (   ord(flag[i]) << 8) 
                 + 
            ord(flag[i + 1])
        )
        for i in range(0, len(flag), 2)
    ]
)

print(flag_encrypted)