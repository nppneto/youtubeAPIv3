from YoutubeAPI import YoutubeAPI
import webbrowser
import pprint
import sys

pp = pprint.PrettyPrinter(indent=2)
youtube = YoutubeAPI()

print("\n")
query = input("Entre com o termo de pesquisa: ").replace(" ", "+")

lists = youtube.search_results(query)

print("\n")
for (key, title) in enumerate(lists['organized_list'], start = 1):
    print("{} - {}".format(key, lists['organized_list'][key]))

print("\n")
print("Qual vídeo deseja assistir? (1, 2, 3...)")
opt = int(input("Caso queira sair, digite 0: "))

if opt == 0:
    print("\n")
    print("Até a próxima!")
    sys.exit()

choosen_title = lists['organized_list'][opt]
choosen_video_url = lists['available_videos'][choosen_title]

webbrowser.open_new(choosen_video_url)

print("\n")
print("O vídeo escolhido foi aberto e executado. Bom divertimento!")
print("\n")