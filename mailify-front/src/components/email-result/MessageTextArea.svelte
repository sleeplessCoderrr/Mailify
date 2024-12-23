<script>
    export let value = '';
    export let placeholder = "Compose your email";
</script>

<textarea
        bind:value
        placeholder={placeholder}
        class="w-full h-96 px-3 py-1.5  rounded border-2 border-stone-300 outline-none"
></textarea>
