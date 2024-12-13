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
    style="width: 100%;
           height: 100%;
           display: block;
           position: fixed;
           top: 0;
           left: 0;
           z-index: -1;">
</canvas>