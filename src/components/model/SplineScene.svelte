<script lang="ts">
    import { onMount } from 'svelte';
    import { Application } from '@splinetool/runtime';
    let canvas: HTMLCanvasElement;
    onMount(() => {
        const app = new Application(canvas);
        app.load('https://prod.spline.design/9XufTzwFSjFQhsqR/scene.splinecode');
    });
</script>

<canvas
    bind:this={canvas}
    style="z-index: -10">
</canvas>
