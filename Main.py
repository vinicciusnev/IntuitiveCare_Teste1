import os
import zipfile
import requests


def main():
   downloadFiles()
   compressFiles()

def downloadFiles():
   ## Saida do diretorio, onde irão os arquivos
   outputDirectory = "C:/Users/Viniccius/Desktop/IntuitiveCare_Teste1/Anexos"

   ## URL's dos arquivos que serão baixados
   urls = [
   "https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.pdf",
   "https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.xlsx",
   "https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN540_RN541_RN542_RN544_546.pdf",
   "https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_III_DC_2021_RN_465.2021.v2.pdf",
   "https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf"
   ]

   ## 
   for url in urls:
      response = requests.get(url)

      if response.status_code == 200:
         file_path = os.path.join(outputDirectory, os.path.basename(url))
         with open(file_path, 'wb') as f:
            f.write(response.content)


# Compactar todos os arquivos em um unico arquivo .zip
def compressFiles():
   with zipfile.ZipFile("Anexos.zip", "w") as myFiles:
      myFiles.write("Anexos/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.pdf", "Anexo1.pdf")
      myFiles.write("Anexos/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN540_RN541_RN542_RN544_546.pdf", "Anexo2.pdf")
      myFiles.write("Anexos/Anexo_III_DC_2021_RN_465.2021.v2.pdf", "Anexo3.pdf")
      myFiles.write("Anexos/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf", "Anexo4.pdf")
      myFiles.write("Anexos/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.xlsx", "Anexo1.xlsx")

main()