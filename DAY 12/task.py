media = ['dance.png','pic.png','mountain.png','forest.png','ice.png','selfie.png','dance.mp4','movie.mp4','singing.mp4']

images = []
videos = []

for file in media:
    if file.endswith('.png'):
        images.append(file)
    elif file.endswith('.mp4'):
        videos.append(file)

print("\n------------Images-----------")
for file in images:
    print(file)

print("\n---------------Videos---------------")
for file in videos:
    print(file)
select = set(input("enter the files to share (using comma):").split())
for file in select:
    if file in media:
        print(f'{file}-sent')
    else:
        print(f"{file}-invalid")
