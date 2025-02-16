<script>
    export let value = '';
    export let placeholder = "Subject";
</script>

<div class="flex items-center space-x-2 mb-2">
    <span class="w-20 text-midnight font-bold">Subject</span>
    <input
            type="text"
            bind:value
            placeholder={placeholder}
            class="flex-1 px-3 py-1.5  rounded border-2 border-stone-300 outline-none"
    />
</div>
