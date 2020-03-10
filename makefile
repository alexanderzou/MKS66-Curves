
run: main.py display.py draw.py matrix.py parse.py pic.py
	python pic.py
	python main.py
	rm face.png
	convert -delay 5 *.png snake.gif

clean:
	rm *.pyc
	rm *~
