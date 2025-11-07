.PHONY : clean
clean :
	rm -f figures/* audio/*
	rm -rf _build/*

build_html:
	myst build --html
