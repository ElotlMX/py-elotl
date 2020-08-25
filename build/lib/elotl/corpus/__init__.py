def list_of_corpus():
    elotl_list_of_corpus = []
    elotl_list_of_corpus.append(['axolotl','Is a nahuatl corpus'])
    elotl_list_of_corpus.append(['tsunkua','Is an otomí corpus'])
    return elotl_list_of_corpus

def load(corpus_name):
    # https://stackoverflow.com/questions/6028000/how-to-read-a-static-file-from-inside-a-python-package
    # l1,l2,variant,document_name
    available_corpus = ['axolotl', 'tsunkua']

    if corpus_name in available_corpus:

        from .. import corpora

        try:
            # For Python >= 3.7
            import importlib.resources as pkg_resources
        except ImportError:
            # Try backported to Python < 3.7 `importlib_resources`.
            import importlib_resources as pkg_resources
        from io import StringIO
        import csv

        corpus_content = pkg_resources.read_text(corpora, corpus_name + '.csv',
            encoding='utf-8', errors='strict')
        corpus_buff = StringIO(corpus_content)
        corpus_reader = csv.reader(corpus_buff)

        return list(corpus_reader)
    else:
        return 0
