import rsa
import base64
from blockchain import Blockchain
from block import Block

chat_blockchain = Blockchain()


def crypto(message, public_key):
    cipher_text = rsa.encrypt(message, public_key)
    return base64.b64encode(cipher_text).decode()


maria_public_key, maria_private_key = rsa.newkeys(512)
joao_public_key, joao_private_key = rsa.newkeys(512)

dado_1 = crypto("Oi, Maria!".encode('utf-8'), joao_public_key)
dado_2 = crypto("Oi, João!".encode('utf-8'), maria_public_key)
dado_3 = crypto("Tudo bem?".encode('utf-8'), joao_public_key)

chat_blockchain.add_block(Block(1, chat_blockchain.get_latest_block().hash, joao_public_key, maria_public_key, dado_1))
chat_blockchain.add_block(Block(2, chat_blockchain.get_latest_block().hash, maria_public_key, joao_public_key, dado_2))
chat_blockchain.add_block(Block(3, chat_blockchain.get_latest_block().hash, joao_public_key, maria_public_key, dado_3))

maria_blocks = chat_blockchain.find_blocks_by_recebedor(maria_public_key)
print("Mensagens de Maria:")
for block in maria_blocks:
    mensagem_descriptografada = rsa.decrypt(base64.b64decode(block.message.encode()), maria_private_key).decode()
    print(f"De: {block.autor} Para: {block.recebedor} Mensagem: {mensagem_descriptografada}")

joao_blocks = chat_blockchain.find_blocks_by_recebedor(maria_public_key)
print("Mensagens de João:")
for block in joao_blocks:
    mensagem_descriptografada = rsa.decrypt(base64.b64decode(block.message.encode()), joao_private_key).decode()
    print(f"De: {block.autor} Para: {block.recebedor} Mensagem: {mensagem_descriptografada}")
