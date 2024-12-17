<script lang="ts">
    import { onMount } from 'svelte';

    let canvas: HTMLCanvasElement;
    let ctx: CanvasRenderingContext2D;
    let particles: { x: number, y: number, velocityX: number, velocityY: number }[] = [];

    const numParticles = 100;

    onMount(() => {
        ctx = canvas.getContext('2d');
        if (ctx) {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            for (let i = 0; i < numParticles; i++) {
                particles.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    velocityX: (Math.random() - 0.5) * 2,
                    velocityY: (Math.random() - 0.5) * 2
                });
            }

            animate();
        }
    });

    function distance(p1: { x: number, y: number }, p2: { x: number, y: number }) {
        return Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = "rgba(255, 99, 74, 0.8)";
        ctx.strokeStyle = "rgba(35, 33, 33, 0.1)";
        ctx.lineWidth = 0.5;

        particles.forEach((p, index) => {
            ctx.beginPath();
            ctx.arc(p.x, p.y, 2, 0, Math.PI * 2);
            ctx.fill();

            let closestDistance = Infinity;
            let closestParticle = null;

            particles.forEach((otherParticle, otherIndex) => {
                if (index !== otherIndex) {
                    const dist = distance(p, otherParticle);
                    if (dist < closestDistance) {
                        closestDistance = dist;
                        closestParticle = otherParticle;
                    }
                }
            });

            if (closestParticle) {
                ctx.beginPath();
                ctx.moveTo(p.x, p.y);
                ctx.lineTo(closestParticle.x, closestParticle.y);
                ctx.stroke();
            }

            p.x += p.velocityX;
            p.y += p.velocityY;

            if (p.x < 0 || p.x > canvas.width) p.velocityX = -p.velocityX;
            if (p.y < 0 || p.y > canvas.height) p.velocityY = -p.velocityY;
        });

        requestAnimationFrame(animate);
    }
</script>

<canvas bind:this={canvas} class="fixed top-0 left-0 z-[-1] bg-mist" />

<style>
    canvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
    }
</style>
