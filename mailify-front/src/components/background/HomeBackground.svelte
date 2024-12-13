<script lang="ts">
    import { onMount } from 'svelte';
    import * as THREE from 'three';
    import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
    import SplineLoader from '@splinetool/loader';

    let canvas: HTMLCanvasElement; // Bind the canvas element

    onMount(() => {
        // Camera
        const camera = new THREE.OrthographicCamera(
            window.innerWidth / -2,
            window.innerWidth / 2,
            window.innerHeight / 2,
            window.innerHeight / -2,
            -50000,
            10000
        );
        camera.position.set(0, 0, 0);
        camera.quaternion.setFromEuler(new THREE.Euler(0, 0, 0));

        // Scene
        const scene = new THREE.Scene();

        // Spline Loader
        const loader = new SplineLoader();
        loader.load('https://prod.spline.design/9XufTzwFSjFQhsqR/scene.splinecode', (splineScene) => {
            scene.add(splineScene);
        });

        // Renderer
        const renderer = new THREE.WebGLRenderer({
            antialias: true,
            canvas, // Use the bound canvas
        });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFShadowMap;
        scene.background = new THREE.Color('#0e0909');
        renderer.setClearAlpha(0);
        scene.fog = new THREE.Fog('#000000', 0, 7500);

        // Orbit Controls
        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.125;

        // Handle Window Resize
        const onWindowResize = () => {
            camera.left = window.innerWidth / -2;
            camera.right = window.innerWidth / 2;
            camera.top = window.innerHeight / 2;
            camera.bottom = window.innerHeight / -2;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        };

        window.addEventListener('resize', onWindowResize);

        // Animation Loop
        const animate = (time: number) => {
            controls.update();
            renderer.render(scene, camera);
        };
        renderer.setAnimationLoop(animate);

        return () => {
            // Cleanup
            window.removeEventListener('resize', onWindowResize);
            renderer.dispose();
        };
    });
</script>

<style lang="scss">
  :root {
    --dark: #000000;
    --light: #17181e;
  }

  canvas {
    background: radial-gradient(circle at 50% 50%, var(--light), var(--dark)) center center / cover;
    background-blend-mode: overlay;
    width: 100%;
    height: 100%;
    display: block;
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;
  }

  body::after {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    background: url('https://www.transparenttextures.com/patterns/noise.png') repeat;
    opacity: 0.2;
    z-index: 1;
  }
</style>

<canvas bind:this={canvas}></canvas>
