import codecs

FLAGS = None

if __name__ == '__main__':

    usage = '''Convert csv annotation to kaldi standard file'''
    parser = argparse.ArgumentParser(description=usage)
    parser.add_argument('csv_dir',
                         help='csv annotation dir')
    FLAGS = parser.parse_args()

    #csv_list = glob.glob('%s/**/*.csv' % FLAGS.csv_dir)
    csv_list = ['csv/62h_1019/32.utf8.csv']
    fid_segment = codecs.open('segments', 'w', 'utf8')
    fid_text = codecs.open('text', 'w', 'utf8')
    for f in csv_list:
        with codecs.open(f, 'r', 'utf8') as fid:
            count = 0
            for line in fid:
                if count == 0:
                    count += 1
                    continue
                row = line.split(',')
                key = row[0]
                content = row[1].strip()
                if re.match('^\[.*\]$', content): continue
                if re.match('^<Broadcast>.*</Broadcast>$', content): continue
                content = re.sub('\[.*\]', '', content)
                content = re.sub('</?overlap>', '', content)
                content = ''.join(re.findall(u'[\u4e00-\u9fff]+', content))
                # drop none chinese character
                src = ''.join(key.split('-')[:-1])
                fid_segment.write('%s %s %s %s\n' % (key, src, row[4], row[5]))
                fid_text.write('%s %s\n' % (key, content))
                count += 1

    fid_segment.close()
    fid_text.close()
