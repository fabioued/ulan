'''
ulan aiml creator & parser
'''

def template(pattern, template):
    return '''
    <category>
        <pattern>{}</pattern>
        <template>{}</template>
    </category>
    '''.format(pattern, template)

def main():
    print template('nama', 'saya')

if __name__ == '__main__':
    main()
