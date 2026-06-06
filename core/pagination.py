import math

def construir_paginacion(
    items,
    total: int,
    page: int,
    size: int,
):
    pages = math.ceil(total/size)
    
    return {
        "items": items,
        "total": total,
        "page": page,
        "size": size,
        "pages": pages
    }