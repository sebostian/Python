import graphics as gr

window = gr.GraphWin("Fractal rectangles", 600, 600)
a = 0.05
def fractal_rectangle(A, B, C, D, deep=10):
	if deep < 1:
		return
	for M, N in (A, B), (B, C), (C, D), (D, A):
		gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
	A1 = (A[0]*(1-a) + B[0]*a, A[1]*(1-a) + B[1]*a)
	B1 = (B[0]*(1-a) + C[0]*a, B[1]*(1-a) + C[1]*a)
	C1 = (C[0]*(1-a) + D[0]*a, C[1]*(1-a) + D[1]*a)
	D1 = (D[0]*(1-a) + A[0]*a, D[1]*(1-a) + A[1]*a)
	fractal_rectangle(A1, B1, C1, D1, deep-1)

fractal_rectangle((100,100), (500, 100), (500, 500), (100, 500), 40)