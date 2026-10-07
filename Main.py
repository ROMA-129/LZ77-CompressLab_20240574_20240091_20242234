import os
from Compression import compress
from Decompression import decompress

def main():
    while True:
        print("\n" + "=" * 40)
        print(" LZ77 Compression & Decompression System")
        print("=" * 40)
        print("1. Compress (Text in file1.txt -> Tags in file2.txt)")
        print("2. Decompress (Tags in file1.txt -> Text in file2.txt)")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == '1':
            if not os.path.exists("file1.txt"):
                print("Error: file1.txt not found!")
                continue
                
            with open("file1.txt", "r", encoding="utf-8") as f:
                original_text = f.read()
                
            tags = compress(original_text)
            
            with open("file2.txt", "w", encoding="utf-8") as f:
                for tag in tags:
                    f.write(f"{tag}\n")
                    
            print("Success: Compressed tags saved to file2.txt")
            
        elif choice == '2':
            if not os.path.exists("file1.txt"):
                print("Error: file1.txt not found!")
                continue
                
            tags = []
            with open("file1.txt", "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        tags.append(eval(line.strip()))
                        
            decompressed_text = decompress(tags)
            
            with open("file2.txt", "w", encoding="utf-8") as f:
                f.write(decompressed_text)
                
            print("Success: Decompressed text saved to file2.txt")
            
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break  
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
