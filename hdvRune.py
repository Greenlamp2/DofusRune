def main():
    put_dofus_front()
    start_retrieval(recherche_word)
    encapsulate_rune(recherche_word)
    generate_excel()
    delete_png()

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))