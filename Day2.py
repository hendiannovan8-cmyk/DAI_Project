print("====Chatbot Saya====")
sistem = input("Tanya apa saja...").lower()

if "dai" in sistem:
    print("DAi adalah singkatan dari Darussalam Artifical Intelegent Forum yang mempelajari tentang bagaimana cara mengenali AI mengembangkan AI sampai membuat AI. ")
elif "ai" in sistem:
    print("AI (Kecerdasan Buatan): Istilah payung yang lebih luas untuk semua teknologi yang membuat mesin terlihat cerdas (bisa berupa aturan logika sederhana maupun sistem yang kompleks).")
elif "mechine learning" in sistem:
    print('Machine Learning (Machine Learning): Salah satu metode di dalam AI agar komputer bisa "belajar sendiri" dari data tanpa harus diprogram secara eksplisit untuk setiap kemungkinan.')
elif sistem:
    print("Maaf kamitidak bisa menjawab pertanyaan anda.")