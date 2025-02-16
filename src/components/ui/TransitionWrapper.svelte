<script lang="ts">
    import { fade, slide } from "svelte/transition";
    export let duration = 300;
    export let transitionType = fade;
</script>

<div transition:fade={{duration}}>
    <slot/>
</div>