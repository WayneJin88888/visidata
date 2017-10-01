#!/usr/bin/env python3

import sys
import yaml


def htmlize(s):
    return s.replace('\\n', '<br>')

# step?, command, [additional] input, result
def body(rows, meta):
    ret = '<h2>{question}</h2>\n'.format(question=meta['question']) 

    # Add asciinema video
    ret += '<asciinema-player id="player" {preview} src="{name}-asciicast.json"></asciinema-player>\n'.format(preview=meta['preview'], name=meta['name'])
    ret += '<script type="text/javascript" src="../asciinema-player.js"></script>\n'
    ret += '<hr/>\n'

    # Add screenshot tutorial
    ret += '<table class="vd">\n'
    ret += ' <tr>\n'
    ret += '  <th>#</th>'
    ret += '  <th>step</th>'
    ret += '  <th>command</th>'
    ret += '  <th>input</th>'
    ret += '  <th>result</th>'
    ret += ' </tr>\n'
    for i, row in enumerate(rows[1:]):
        colname = '<span class="code">%s</span> column' % row[1]
        ret += ' <tr>\n'
        ret += '  <td class="timestamp"><a id="step{stepnum}" title="Click to jump to this timestamp in the video" href="#" onclick="setTime({timestamp});return false;">{stepnum}</a></td>\n'.format(stepnum=i+1, timestamp=meta['timestamps'][i])
        ret += '  <td class="step">%s</td>' % (htmlize(row[5]).replace("current column", colname))
        ret += '  <td class="command">%s</td>' %  htmlize(row[3])
        ret += '  <td class="input">%s</td>' %  htmlize(row[4])
        #ret += '  <td class="screenshot"><img src="%s.png" alt=""/></td>\n' % (i+1)

        ret += ' </tr>\n'
    ret += '</table>\n'
    ret += '<hr/>\n'
    
    return ret


def main(yamlfn):
    meta = yaml.load(open(yamlfn).read())
    rows = list(row[:-1].split('\t') for row in open(meta['vd']))
    print(body(rows, meta))

main(*sys.argv[1:])


