args = "use_grid=False,browser=chrome,timeout=30,folder=current_regression"
if args is not None:
    for arg in args.split(","):
        if "folder" not in arg:
            print(arg)

