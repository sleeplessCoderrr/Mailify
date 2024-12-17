<script lang="ts">
    export let categories: string[];
    export let activeCategory: string;
    export let setActiveCategory: (category: string) => void;
</script>

<div class="flex space-x-4 mt-6">
    {#each categories as category}
        <button
                class={`py-2 px-4 rounded border-2 border-stone-300 ${
        activeCategory === category ? "bg-blaze text-white" : "bg-mist text-midnight"
      }`}
                on:click={() => setActiveCategory(category)}
        >
            {category}
        </button>
    {/each}
</div>
