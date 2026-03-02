from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Producto


# ========================================
# 1. READ - LISTAR TODOS LOS PRODUCTOS (GET)
# ========================================
def api_lista_productos(request):
    if request.method == 'GET':
        productos = Producto.objects.all().values(
            'id', 
            'nombre', 
            'precio', 
            'stock', 
            'categoria', 
            'descripcion',
            'fecha_creacion',
            'fecha_actualizacion'
        )
        return JsonResponse(list(productos), safe=False, status=200)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)


# ========================================
# 2. CREATE - CREAR UN PRODUCTO (POST)
# ========================================
@csrf_exempt
def api_crear_producto(request):
    if request.method == 'POST':
        try:
            # Intentar cargar datos desde JSON
            data = json.loads(request.body)
            
            # Validar que los campos requeridos estén presentes
            if not data.get('nombre'):
                return JsonResponse({'error': 'El campo nombre es requerido'}, status=400)
            if not data.get('precio'):
                return JsonResponse({'error': 'El campo precio es requerido'}, status=400)
            if data.get('stock') is None:
                return JsonResponse({'error': 'El campo stock es requerido'}, status=400)
            if not data.get('categoria'):
                return JsonResponse({'error': 'El campo categoria es requerido'}, status=400)
            
            # Crear el producto
            producto = Producto.objects.create(
                nombre=data.get('nombre'),
                precio=float(data.get('precio')),
                stock=int(data.get('stock')),
                categoria=data.get('categoria'),
                descripcion=data.get('descripcion', '')
            )
            
            return JsonResponse({
                'mensaje': 'Producto registrado exitosamente',
                'id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio,
                'stock': producto.stock,
                'categoria': producto.categoria
            }, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
        except ValueError as e:
            return JsonResponse({'error': f'Error en los datos: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Error al crear producto: {str(e)}'}, status=500)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)


# ========================================
# 3. UPDATE - ACTUALIZAR UN PRODUCTO (PUT)
# ========================================
@csrf_exempt
def api_actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            
            # Actualizar solo los campos que fueron enviados
            if 'nombre' in data:
                producto.nombre = data['nombre']
            if 'precio' in data:
                producto.precio = float(data['precio'])
            if 'stock' in data:
                producto.stock = int(data['stock'])
            if 'categoria' in data:
                producto.categoria = data['categoria']
            if 'descripcion' in data:
                producto.descripcion = data['descripcion']
            
            producto.save()
            
            return JsonResponse({
                'mensaje': 'Producto actualizado exitosamente',
                'id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio,
                'stock': producto.stock,
                'categoria': producto.categoria
            }, status=200)
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
        except ValueError as e:
            return JsonResponse({'error': f'Error en los datos: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Error al actualizar producto: {str(e)}'}, status=500)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)


# ========================================
# 4. DELETE - ELIMINAR UN PRODUCTO (DELETE)
# ========================================
@csrf_exempt
def api_eliminar_producto(request, pk):
    if request.method == 'DELETE':
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
        
        return JsonResponse({}, status=204)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)
