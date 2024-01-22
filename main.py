from eth_account import Account
from eth_account.signers.local import LocalAccount
import secrets

print()

def create_wallets(amount, file_name, file_format, type_wallet, K=None):
    Account.enable_unaudited_hdwallet_features()
    delimiter = ':' if file_format == 0 else ','
    header = 'Address' + delimiter + 'Private Key'
    file_extension = '.txt' if file_format == 0 else '.csv'

    if type_wallet == 0:
        header += delimiter + 'Mnemonic'

    with open(f'{file_name}{file_extension}', 'a') as f:
        f.write(header + '\n')
        for _ in range(int(amount)):
            if type_wallet == 0:
                new_acc, mnemonic = Account.create_with_mnemonic(num_words=int(K))
                f.write(f'{new_acc.address}{delimiter}{new_acc._private_key.hex()}{delimiter}{mnemonic}\n')
            elif type_wallet == 1:
                key = '0x' + secrets.token_hex(32)
                new_acc = Account.from_key(key)
                f.write(f'{new_acc.address}{delimiter}{new_acc._private_key.hex()}\n')
    print(f'\nВаши кошельки готовы в файле {file_name}{file_extension}\nЕщё больше интересного в канале https://t.me/Eazercrypto')

K = None
type_wallet = int(input("Выбирете тип кошельков: \n[0] Address + Prkey + Mnemonic\n[1] Address + Prkey\nВаш выбор: "))
amount = input("\nВведите, сколько кошельков создать: ")

if type_wallet == 0:
    K = input("\nСколько слов использовать для мнемоника(доступно 12,15,18,21,24): ")

file_name = input('\nВведите название файла для кошельков: ')
file_format = int(input("\nВыбирете тип файла для сохранения: \n[0] .txt\n[1] .csv\nВаш выбор: "))

create_wallets(amount, file_name, file_format, type_wallet, K)