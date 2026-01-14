import * as THREE from 'three';

// Inicjalizacja p5 w trybie "instance". 
// Tworzymy obiekt 'p', aby mieć dostęp do funkcji matematycznych p5 (jak noise i map) 
// bez tworzenia standardowego płótna (canvas) p5.js.
const p = new p5();

class Walker {
  constructor() {
    // currentPos przechowuje aktualne współrzędne w przestrzeni 3D
    this.currentPos = new THREE.Vector3(0, 0, 0);
    
    // Maksymalna długość pojedynczego kroku
    this.stepSize = 0.2;
    
    // "Czas" (offsety) dla szumu Perlina dla każdej osi.
    // Ustawiamy je daleko od siebie (np. 0, 10000, 20000), 
    // aby ruchy w osiach X, Y i Z nie były identyczne (były niezależne).
    this.tx = 0;
    this.ty = 10000;
    this.tz = 20000;

    // --- Wizualizacja obiektu w Three.js ---
    // Tworzymy geometrię kostki o wymiarach 5x5x5 jednostek
    this.cubeGeometry = new THREE.BoxGeometry(5, 5, 5);
    // Tworzymy prosty materiał w kolorze zielonym (nie reaguje na światło)
    this.cubeMaterial = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    // Łączymy geometrię z materiałem w jeden obiekt (Mesh)
    this.cube = new THREE.Mesh(this.cubeGeometry, this.cubeMaterial);
    
    // Dodajemy kostkę bezpośrednio do sceny zdefiniowanej niżej
    scene.add(this.cube);
  }

  update() {
    // Pobieramy wartość szumu Perlina (zawsze zwraca liczbę od 0 do 1)
    let nx = p.noise(this.tx);
    let ny = p.noise(this.ty);
    let nz = p.noise(this.tz);

    // Mapujemy wartość 0-1 na zakres od -stepSize do +stepSize.
    // Dzięki temu kostka może poruszać się w obie strony w każdej osi.
    let stepX = p.map(nx, 0, 1, -this.stepSize, this.stepSize);
    let stepY = p.map(ny, 0, 1, -this.stepSize, this.stepSize);
    let stepZ = p.map(nz, 0, 1, -this.stepSize, this.stepSize);
    
    // Aktualizujemy wektor pozycji o wyliczony krok (Random Walk oparty na szumie)
    this.currentPos.x += stepX;
    this.currentPos.y += stepY;
    this.currentPos.z += stepZ;
    
    // --- Logika granic ---
    // Definiujemy limity, po których przekroczeniu kostka wraca do punktu zero.
    // Uwaga: W Three.js jednostki to nie piksele, więc innerWidth/Height są tu bardzo dużymi wartościami.
    const limitX = innerWidth / 20; // Przykładowe przeskalowanie limitów
    const limitY = innerHeight / 20;
    const limitZ = 200;
    
    // Sprawdzanie granic i resetowanie pozycji do (0,0,0) jeśli kostka ucieknie za daleko
    if (this.currentPos.x > limitX || this.currentPos.x < -limitX) this.currentPos.x = 0;
    if (this.currentPos.y > limitY || this.currentPos.y < -limitY) this.currentPos.y = 0;
    if (this.currentPos.z > limitZ || this.currentPos.z < 0) this.currentPos.z = 0;
    
    // Zwiększamy "czas" dla szumu Perlina. 
    // Im mniejsza wartość (np. 0.005), tym ruch jest płynniejszy i bardziej "organiczny".
    this.tx += 0.005;
    this.ty += 0.005;
    this.tz += 0.005;

    // Przypisujemy obliczoną pozycję do fizycznego obiektu kostki w scenie
    this.cube.position.copy(this.currentPos);
  }
}

// --- Konfiguracja Sceny Three.js ---

// 1. Scena - kontener na wszystkie obiekty
const scene = new THREE.Scene();

// 2. Kamera - określa co widzimy (kąt widzenia, proporcje, bliska i daleka płaszczyzna cięcia)
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
// Odsuwamy kamerę na osi Z, aby widzieć obiekty na środku sceny
camera.position.z = 200;

// 3. Renderer - silnik rysujący scenę na ekranie (WebGL)
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight); // Ustawienie wielkości okna
document.body.appendChild(renderer.domElement); // Dodanie płótna Three.js do strony HTML

// Tworzymy instancję naszej klasy Walker
const walker = new Walker();

// --- PĘTLA ANIMACJI ---
// Funkcja wywoływana około 60 razy na sekundę
function animate() {
  requestAnimationFrame(animate);

  // Aktualizujemy logikę walkera (ruch, szum, pozycję)
  walker.update();

  // Dodajemy delikatny obrót całej sceny, aby wzmocnić efekt 3D
  scene.rotation.y += 0.005;

  // Renderujemy (rysujemy) klatkę obrazu z perspektywy kamery
  renderer.render(scene, camera);
}

// Uruchomienie pętli animacji
animate();