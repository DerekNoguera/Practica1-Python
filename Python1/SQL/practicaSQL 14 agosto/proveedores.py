proveedores = [
    {
        "id": 1,
        "name": "proveedor 1"
    },
    {
        "id": 2,
        "name": "proveedor 2"
    }
]
productos = [
    {
        "id": 1,
        "name": "producto 1",
        "precio": 11,
        "proveedor_id": 1
    },
    {
        "id": 2,
        "name": "producto 2",
        "precio": 15,
        "proveedor_id": 2
    },
    {
        "id": 3,
        "name": "producto 3",
        "precio": 10,
        "proveedor_id": 1
    },
    {
        "id": 4,
        "name": "producto 4",
        "precio": 20,
        "proveedor_id": 2
    }
]

resultado_proveedores_con_productos_baratos = []
resultado_proveedores_con_productos_caros = []

for proveedor in proveedores:
    flag = False
    for producto in productos:
        if (producto.proveedor_id == proveedor.id and producto.precio <= 10):
            flag = True
            resultado_proveedores_con_productos_baratos.append(proveedor)#esto lo hace si usamos Exists
            continue
    if(flag == False):
        resultado_proveedores_con_productos_caros.append(proveedor)