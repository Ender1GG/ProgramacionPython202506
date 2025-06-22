barra_pan_vendidas_xdia=int(input())
barra_pan=3.49
barra_pan_nodia=barra_pan*0.6
precio_final=barra_pan_vendidas_xdia*barra_pan_nodia
print(f'el precio de una barra de pan normal es: {barra_pan}'  )
print(f'descuento por no ser del dia: {barra_pan_nodia}')
print(round(precio_final))