    # create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    t = time.time()
    # start the processes
    p1.start()
    p2.start()


    p1.join()
    p2.join()

    finished_time = time.time()-t
    print(f'Time taken without multi processing: {finished_time}')

    