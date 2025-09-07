def main():
   
    frutas = []
    
    frutas.append("mango")
    frutas.append("Manzana")
    frutas.append("Banana")
    frutas.append("uvas")
    
    print("Lista inicial:", frutas)
    
   
    frutas.pop(0)  
    frutas.pop(1)  
    
    frutas.append("sandia")
    
    print("Lista final:", frutas)


if __name__ == "__main__":
    main()
