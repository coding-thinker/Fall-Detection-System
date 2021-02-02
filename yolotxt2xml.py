import os
from PIL import Image
root_dir = "./VOC2007/"
annotations_dir = root_dir + "Annotations/"  # 这里是Annotations文件夹的路径
image_dir = root_dir + "JPEGImages/"  # 这里是JPEGImages文件夹的路径
xml_dir = root_dir + "Annotations_XML/"  # 这个文件夹先建立出来，里面是空的
class_name = [] # here add class names (in accordance with line[0] index)

for filename in os.listdir(annotations_dir):
    fin = open(annotations_dir + filename, 'r')
    image_name = filename.split('.')[0]
    img = Image.open(image_dir + image_name + ".jpg")
    xml_name = xml_dir + image_name + '.xml'
    with open(xml_name, 'w') as fout:
        Pwidth, Pheight = img.size
        fout.write('<annotation>' + '\n')

        fout.write('\t' + '<folder>VOC2007</folder>' + '\n')
        fout.write('\t' + '<filename>' + image_name + '.jpg' + '</filename>' + '\n')

        fout.write('\t' + '<source>' + '\n')
        fout.write('\t\t' + '<database>' + 'VisDrone2018 Database' + '</database>' + '\n')
        fout.write('\t\t' + '<annotation>' + 'VOC2007' + '</annotation>' + '\n')
        fout.write('\t\t' + '<image>' + 'flickr' + '</image>' + '\n')
        fout.write('\t\t' + '<flickrid>' + 'Unspecified' + '</flickrid>' + '\n')
        fout.write('\t' + '</source>' + '\n')

        fout.write('\t' + '<owner>' + '\n')
        fout.write('\t\t' + '<flickrid>' + 'liwang' + '</flickrid>' + '\n')
        fout.write('\t\t' + '<name>' + 'liwang' + '</name>' + '\n')
        fout.write('\t' + '</owner>' + '\n')

        fout.write('\t' + '<size>' + '\n')
        fout.write('\t\t' + '<width>' + str(img.size[0]) + '</width>' + '\n')
        fout.write('\t\t' + '<height>' + str(img.size[1]) + '</height>' + '\n')
        fout.write('\t\t' + '<depth>' + '3' + '</depth>' + '\n')
        fout.write('\t' + '</size>' + '\n')

        fout.write('\t' + '<segmented>' + '0' + '</segmented>' + '\n')

        for line in fin.readlines():
            line = line.strip().split(' ')
            fout.write('\t' + '<object>' + '\n')
            fout.write('\t\t' + '<name>' + class_name[int(line[0])] + '</name>' + '\n')
            fout.write('\t\t' + '<pose>' + 'Unspecified' + '</pose>' + '\n')
            fout.write('\t\t' + '<truncated>' + '0' + '</truncated>' + '\n')
            fout.write('\t\t' + '<difficult>' + '0' + '</difficult>' + '\n')
            fout.write('\t\t' + '<bndbox>' + '\n')
            mathData = int(((float(line[1]))*Pwidth+1)-(float(line[3]))*0.5*Pwidth)
            fout.write('\t\t\t' + '<xmin>' + str(mathData) + '</xmin>' + '\n')
            mathData = int(((float(line[2]))*Pheight+1)-(float(line[4]))*0.5*Pheight)
            fout.write('\t\t\t' + '<ymin>' + str(mathData) + '</ymin>' + '\n')

            # pay attention to this point!(0-based)
            
            mathData = int(((float(line[1]))*Pwidth+1)+(float(line[3]))*0.5*Pwidth)
            fout.write('\t\t\t' + '<xmax>' + str(mathData) + '</xmax>' + '\n')
            mathData = int(((float(line[2]))*Pheight+1)+(float(line[4]))*0.5*Pheight)
            fout.write('\t\t\t' + '<ymax>' + str(mathData) + '</ymax>' + '\n')
            fout.write('\t\t' + '</bndbox>' + '\n')
            fout.write('\t' + '</object>' + '\n')

        fin.close()
        fout.write('</annotation>')
